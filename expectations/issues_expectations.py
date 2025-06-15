from great_expectations.core.expectation_suite import ExpectationSuite
import great_expectations.expectations as gxe
import great_expectations as gx


def build_expectation_suite() -> ExpectationSuite:
    context = gx.get_context()
    expectation_suite_name = "expectations_github_issues"
    suite = context.suites.add_or_update(
        gx.core.expectation_suite.ExpectationSuite(name=expectation_suite_name)
    )

    # Adicione suas expectativas aqui
    suite.add_expectation(
        gxe.ExpectColumnMaxToBeBetween(column="number", max_value=18000)
    )
    suite.add_expectation(gxe.ExpectColumnToExist(column="number"))

    suite.add_expectation(
        gxe.ExpectColumnValuesToBeBetween(column="number", min_value=1, max_value=18000)
    )

    return suite


if __name__ == "__main__":
    build_expectation_suite()
