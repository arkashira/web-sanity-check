# ROADMAP.md

## Roadmap for Web Sanity Check

### MVP Milestone

The MVP milestone focuses on delivering a functional core product that addresses the primary need of identifying and prioritizing flaky tests. This will ensure that users can start benefiting from the tool immediately upon launch.

#### Core Features (MVP-Critical)
- **Instance Creation**: Implement the ability to create an instance of `WebSanityCheck`. This includes setting up the necessary configuration options and initializing any required data structures. 
- **Test Result Addition**: Develop the `add_test_result` method to allow users to input test results. This should include validation checks to ensure data integrity.
- **Flaky Test Identification**: Implement the `get_flaky_tests` method to analyze added test results and identify which tests exhibit flaky behavior. Define clear criteria for what constitutes a flaky test.
- **Investigation Tracking**: Create the `mark_test_as_investigated` method to allow users to mark tests that have been reviewed or fixed. This will help in tracking progress and ensuring that flaky tests are addressed systematically.

### Version 1 Phase

The v1 phase aims to enhance the core functionality by adding features that improve usability and provide deeper insights into test stability.

#### Themes
- **Enhanced Analysis**
- **User Experience Improvements**

##### Enhanced Analysis
- **Advanced Flaky Test Metrics**: Introduce additional metrics to provide more detailed information about flaky tests, such as frequency, impact on build times, and historical trends.
- **Correlation Analysis**: Implement a feature to analyze correlations between flaky tests and other factors like environment variables, code changes, or specific test conditions.

##### User Experience Improvements
- **User Interface**: Develop a simple command-line interface (CLI) or a basic web interface to make interaction with the tool more intuitive and user-friendly.
- **Documentation and Examples**: Expand the documentation to include detailed usage examples, best practices, and troubleshooting guides.

### Version 2 Phase

The v2 phase focuses on integrating advanced features and expanding the tool's capabilities to support larger and more complex testing environments.

#### Themes
- **Integration and Scalability**
- **Automation and Reporting**

##### Integration and Scalability
- **CI/CD Integration**: Enable seamless integration with popular CI/CD platforms to automatically collect test results and trigger analysis workflows.
- **Scalable Architecture**: Optimize the tool's architecture to handle large volumes of test data efficiently, ensuring performance even in high-scale environments.

##### Automation and Reporting
- **Automated Investigation**: Implement automated processes to investigate potential causes of flaky tests based on predefined rules and patterns.
- **Comprehensive Reporting**: Develop advanced reporting features that generate detailed reports summarizing test stability, investigation status, and recommendations for improvement.

By following this roadmap, the Web Sanity Check project will evolve from a basic tool for identifying flaky tests into a comprehensive solution that supports efficient test stabilization and enhances overall software quality.
