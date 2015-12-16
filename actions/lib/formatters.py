__all__ = [
    'issue_to_dict',
    'label_to_dict'
]


def issue_to_dict(issue):
    result = {}

    if issue.closed_by:
        closed_by = issue.closed_by.name
    else:
        closed_by = None

    if issue.user:
        author = issue.user.name
    else:
        author = None

    if issue.assignee:
        assignee = issue.assigne.name
    else:
        assignee = None

    if issue.pull_request:
        is_pull_request = True
    else:
        is_pull_request = False

    result['id'] = issue.id
    result['repository'] = issue.repository.name
    result['author'] = author
    result['assign'] = assignee
    result['title'] = issue.title
    result['body'] = issue.body
    result['url'] = issue.html_url
    result['state'] = issue.state
    result['is_pull_request'] = is_pull_request

    if issue.labels:
        labels = [label_to_dict(label) for label in issue.labels]
    else:
        labels = []

    result['labels'] = labels
    result['created_at'] = issue.created_at
    result['closed_at'] = issue.closed_at
    result['closed_by'] = closed_by
    return result


def label_to_dict(label):
    result = {}

    result['name'] = label.name
    result['color'] = label.color
    result['url'] = label.url

    return result
