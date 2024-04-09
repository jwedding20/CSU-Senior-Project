Jeff Wedding

Computer Science (B.S)  
Dr. Sean Hayes

Test Plan Specification

Introduction: This test plan involves a multi-faceted approach to ensure the game’s functionality, performance, and reliability across various scenarios. The primary goal is to verify seamless gameplay between two players on separate computers while adhering to the rules of checkers. Constraints include compatibility testing across different network environments to guarantee smooth communication and synchronization between players. Performance testing will be conducted to assess the game's functionality. Overall, the test plan aims to deliver a robust and enjoyable gaming experience.

References: Project Proposal, Requirements Specification, Test Plan Specification

Test Items: PowerShell 5.1, Python 3.11, Pygame 2.6

Features to be Tested: Functionality of the game including but not limited to: players are able to move and jump over pieces, players are able to “double jump”, pawns turn into kings if they reach the other side of the board, game will end once a player has collected all of the opponent’s pieces. The connection between the two players will also be tested.

Features Not to be Tested: N/A

Approach: The most logical approach to testing this program involves both manual and white box testing methods. Manual testing entails simulating various game scenarios, such as different moves, captures, and game-ending conditions, to ensure smooth gameplay and accurate rule enforcement. White-box testing involves examining the game's source code to identify potential bugs or vulnerabilities, such as incorrect game state handling or network communication errors, ensuring robustness and reliability. By combining these approaches, the testing process aims to deliver a polished and error-free experience for players.

Item Pass/Fail Criteria: There will be an expected outcome for each test. If the expected outcome matches the actual outcome, the test is considered passing. If not, the test is considered a failure.

Suspension Criteria and Resumption Requirements: N/A

Test Deliverables: Test plan, Test cases

Test Environment: Powershell, Python, Pygame, Microsoft Word

Schedule:

- April 8, 2024: Turn in test plan.
- Mid-April 2024: Finish networking portion of the program.
- Late-April 2024: Begin testing.
- Summer 2024: Make any necessary changes.
- Fall 2025: Senior Project Defense

Risks: There may be some security vulnerabilities within the program, as I have not learned how to test for them. Furthermore, I have very little experience in network communication protocols, so I do not yet know how to identify and test vulnerabilities within the network. I will reduce this risk by researching proper techniques for creating communication over a network without risk.

Assumptions and Dependencies: There are no dependencies within my test plan. However, my test plan assumes that I will complete the network side of the project in the next couple of weeks. My test plan also assumes that testing will not take very long.

Approvals: Dr. Sean Hayes