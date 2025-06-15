import great_expectations as gx
import great_expectations.expectations as gxe
from expectations.issues_expectations import build_expectation_suite


def setup_context():
    context = gx.get_context()
    datasource = context.data_sources.add_or_update_sql(
        "mysql-source",
        connection_string="mysql+pymysql://admin:l123@localhost:3306/github_issues",
    )
    data_asset = datasource.add_table_asset(
        name="github_issues", table_name="issues", schema_name="github_issues"
    )
    batch_definition = data_asset.add_batch_definition_whole_table(
        "my batch definition"
    )

    return context, batch_definition


if __name__ == "__main__":
    context, batch_definition = setup_context()
    suite = build_expectation_suite()

    batch = batch_definition.get_batch()

    validation_definition = context.validation_definitions.add_or_update(
        gx.core.validation_definition.ValidationDefinition(
            name="validations_github_issues", data=batch_definition, suite=suite
        )
    )

    checkpoint = context.checkpoints.add_or_update(
        gx.checkpoint.checkpoint.Checkpoint(
            name="github_issues_checkpoint",
            validation_definitions=[validation_definition],
        )
    )

    checkpoint_res = checkpoint.run()
    print(checkpoint_res.describe())
