## OpenEuler Community Command Help

All of the projects in OpenEuler Community are maintained by Bot.
That means the developpers can comment below every pull requst or issue to trigger Bot Commands.
The Commands incluing as follows:

<table class="command">
    <thead>
        <tr>
            <th>Command</th>
            <th>Example</th>
            <th>Description</th>
            <th>Who Can Use</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                /check-cla
            </td>
            <td>
                /check-cla
            </td>
            <td>
                Forces rechecking of the CLA status of a Pull Request.
                If the Pull Request author has already signed CLA,
                the label `autopeneuler-cla/yes` will be added in the Pull Request,
                If not, the label `autopeneuler-cla/no` will be added.
            </td>
            <td>
                Anyone
            </td>
        </tr>
        <tr>
            <td>
                /lgtm [cancel]
            </td>
            <td>
                /lgtm
                <br/>
                /lgtm cancel
            </td>
            <td>
                Adds or removes the 'lgtm' label which is typically used to gate merging.
            </td>
            <td>
                Collaborators on the repository. '/lgtm cancel' can be used additionally by the Pull Request author.
            </td>
        </tr>
        <tr>
            <td>
                /approve [cancel]
            </td>
            <td>
                /approve
                <br/>
                /approve cancel
            </td>
            <td>
                Adds or removes the 'approved' label which is typically used to gate merging.
            </td>
            <td>
                Collaborators on the repository.
            </td>
        </tr>
        <tr>
            <td>
                /[remove-]kind
            </td>
            <td>
                /kind bug
                <br/>
                /remove-kind bug
            </td>
            <td>
                Applies or removes a kind label from one of the recognized types of labels.
                For example, the label is more like `kind/bug`.
            </td>
            <td>
                Anyone can trigger this command on a Pull Request or Issue.
            </td>
        </tr>
        <tr>
            <td>
                /[remove-]priority
            </td>
            <td>
                /priority high
                <br/>
                /remove-priority high
            </td>
            <td>
                Applies or removes a priority label from one of the recognized types of labels.
                For example, the label is more like `priority/high`.
            </td>
            <td>
                Anyone can trigger this command on a Pull Request or Issue.
            </td>
        </tr>
        <tr>
            <td>
                /[remove-]sig
            </td>
            <td>
                /sig kernal
                <br/>
                /remove-sig kernal
            </td>
            <td>
                Applies or removes a sig label from one of the recognized types of labels.
                For example, the label is more like `sig/kernal`.
            </td>
            <td>
                Anyone can trigger this command on a Pull Request or Issue.
            </td>
        </tr>
    </tbody>
</table>
