from behave import *

from automation_factory import package_sort


@given("the robot arm is ready")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when(
    "a package with width {width:d}, height {height:d}, length {length:d}, and mass {mass:d} is given"
)
def step_impl(context, width, height, length, mass):
    """
    :type context: behave.runner.Context
    :type width: str
    :type height: str
    :type length: str
    :type mass: str
    """
    context.stack = package_sort(width, height, length, mass)


@then("the package is classified as {classification}")
def step_impl(context, classification):
    """
    :type context: behave.runner.Context
    :type classification: str
    """
    assert context.stack is not None
    assert context.stack == classification
