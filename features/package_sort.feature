Feature: Classify packages according to size and weight

  Scenario Outline: classify package based on dimensions and mass
    Given the robot arm is ready
    When a package with width <width>, height <height>, length <length>, and mass <mass> is given
    Then the package is classified as <classification>

    Examples:
      | width | height | length | mass | classification |
      | 50    | 50     | 50     | 10   | STANDARD       |
      | 50    | 50     | 50     | 25   | SPECIAL        |
      | 100   | 100    | 100    | 10   | SPECIAL        |
      | 160   | 100    | 100    | 10   | SPECIAL        |
      | 100   | 160    | 100    | 10   | SPECIAL        |
      | 100   | 100    | 160    | 10   | SPECIAL        |
      | 100   | 100    | 100    | 25   | REJECTED       |
      | 160   | 100    | 100    | 25   | REJECTED       |
      | 50    | 50     | 50     | 20   | SPECIAL        |
      | 99    | 100    | 100    | 19   | STANDARD       |
      | 101   | 101    | 101    | 21   | REJECTED       |
