const getHeadBranch = () => {
    if (context.eventName === 'pull_request') {
        return context.payload.pull_request.head.ref;
    } else if (context.eventName === 'push') {
        return context.ref.replace('refs/heads/', '');
    } else {
        return context.ref.replace('refs/heads/', '');
    }
};

const headBranch = getHeadBranch();
const baseBranch = 'sandbox';

console.log(`Head branch: ${headBranch}`);
console.log(`Base branch: ${baseBranch}`);

// Check if PR already exists
const { data: prs } = await github.rest.pulls.list({
owner: context.repo.owner,
repo: context.repo.repo,
head: `${context.repo.owner}:${headBranch}`,
base: baseBranch,
state: 'open'
});

let pr;
if (prs.length === 0) {
// Create new PR
try {
    const { data: newPr } = await github.rest.pulls.create({
    owner: context.repo.owner,
    repo: context.repo.repo,
    title: `🔄 Terraform changes from ${headBranch}`,
    head: headBranch,
    base: baseBranch,
    body: '🚀 This PR contains Terraform changes.'
    });
    pr = newPr;
} catch (error) {
    console.error('Error creating PR:', error.message);
    return;
}
} else {
    pr = prs[0];
}

function getStatusSummary(status, planStatus, add, change, destroy) {
    if (status !== 'Success') return `❌ Plan ${status}`;

    switch (planStatus) {
        case 'planned':
        if (destroy > 0) return '🚨 Destructive changes detected';
        if (change > 0) return '⚠️ Resource modifications planned';
        if (add > 0) return '✨ New resources to be added';
        return '✅ No changes required';
        case 'pending':
        return '⏳ Plan pending';
        case 'running':
        return '🔄 Plan in progress';
        case 'errored':
        return '🚫 Plan encountered an error';
        case 'canceled':
        return '🛑 Plan was canceled';
        case 'cost_estimated':
        return '💰 Cost estimation completed';
        case 'policy_checked':
        return '📋 Policy check completed';
        case 'planned_and_finished':
        return '🏁 Plan completed and finished';
        default:
        return `ℹ️ Plan status: ${planStatus}`;
    }
}

const statusSummary = getStatusSummary(
'${{ needs.terraform-plan.outputs.status }}',
'${{ needs.terraform-plan.outputs.plan_status }}',
'${{ needs.terraform-plan.outputs.add }}',
'${{ needs.terraform-plan.outputs.change }}',
'${{ needs.terraform-plan.outputs.destroy }}'
);

const planOutput = `### 🔍 Terraform Plan Results

${statusSummary}

\`\`\`diff
+ Plan: ${{ needs.terraform-plan.outputs.add }} to add
~ ${{ needs.terraform-plan.outputs.change }} to change
- ${{ needs.terraform-plan.outputs.destroy }} to destroy
\`\`\`

📊 [View full plan details](${{ needs.terraform-plan.outputs.run_link }})

Additional Information:
- Operation Result: ${{ needs.terraform-plan.outputs.status }}
- Plan ID: ${{ needs.terraform-plan.outputs.plan_id }}

---
⚠️ Please review these changes carefully before merging.
`

await github.rest.issues.createComment({
    owner: context.repo.owner,
    repo: context.repo.repo,
    issue_number: pr.number,
    body: planOutput
});