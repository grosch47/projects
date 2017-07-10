success_a <- 52
success_b <- 44
sample_a <- 1253
sample_b <- 1226
#two-sample proportion test 
#because we are determing if conversion rates are different between two groups
prop.test(x=c(success_a, success_b), n=c(sample_a, sample_b), 
          alternative = "greater", #one-sided because we are only interested in detecting growth. is A > B ?
          conf.level = .90) #90% confidence
