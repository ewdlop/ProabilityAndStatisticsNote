# Function to check if a package is installed, and install it if it's not
install_if_missing <- function(package_name) {
  if (!require(package_name, character.only = TRUE)) {
    install.packages(package_name, dependencies = TRUE)
    library(package_name, character.only = TRUE)
  }
}

# Example usage
install_if_missing("bayesrules")  # Replace "bayesrules" with the package you want to install

# Define the prior probability
prior <- c(0.5, 0.5)  # Prior probabilities for two hypotheses H1 and H2

# Define the likelihood of observing the data under each hypothesis
likelihood <- c(0.7, 0.2)  # Likelihood of observing the data D given H1 and H2

# Calculate the marginal likelihood
marginal_likelihood <- sum(prior * likelihood)

# Calculate the posterior probability
posterior <- (prior * likelihood) / marginal_likelihood

# Print the posterior probabilities
print(posterior)
