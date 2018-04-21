Feature: Compute the frequence or wavelength
  In order to see if the wavelength or frequence can be calculated 
  As a user
  We try the calculation

  Scenario: Frequence of 0.0
    Given I have a wavelength of 0.0
    When I compute the frequence
    Then I receive 0.0

  Scenario: Frequence of 100.0
    Given I have a wavelength of 100.0
    When I compute the frequence
    Then I receive 2997924.58

  Scenario: Wavelength of 0.0
    Given I have a frequence of 0.0
    When I compute the wavelength
    Then I receive 0.0

  Scenario: Wavelength of 0.4
    Given I have a frequence of 0.4
    When I compute the wavelength
    Then I receive 749481145.0

  
