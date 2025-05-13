# install.packages(c("tidyverse", "lubridate", "corrplot"))

library(tidyverse)
library(lubridate)
library(corrplot)

# 1) Load & clean
df <- read_csv("data/raw/SDCounty_WQ_2017-2023.csv") %>%
  rename(
    Location = `Location/county`,
    Date     = Quarter_DDMMYYYY
  ) %>%
  mutate(Date = mdy(Date)) %>%
  arrange(Date)

# 2) Correlation matrix of all numeric parameters
num_mat <- df %>%
  select(Temp, pH, Turbidity, DO, TDS) %>%
  na.omit() %>%
  cor()

corrplot(
  num_mat,
  method      = "color",
  addCoef.col = "black",
  number.cex  = 0.7,
  tl.cex      = 0.8,
  title       = "Correlation Matrix of Water-Quality Parameters",
  mar         = c(0,0,1,0)
)

# 3) County-wide quarterly averages
avg_df <- df %>%
  group_by(Date) %>%
  summarize(
    Temp      = mean(Temp,      na.rm = TRUE),
    pH        = mean(pH,        na.rm = TRUE),
    Turbidity = mean(Turbidity, na.rm = TRUE),
    DO        = mean(DO,        na.rm = TRUE),
    TDS       = mean(TDS,       na.rm = TRUE)
  ) %>%
  arrange(Date)

# 4) Helper to extract CCF into a tibble
get_ccf_df <- function(x, y, lag.max = 8, name) {
  r <- ccf(x, y, lag.max = lag.max, plot = FALSE)
  tibble(
    lag  = as.integer(r$lag),
    ccf  = as.numeric(r$acf),
    pair = name
  )
}

# 5) Compute two lead–lag series: DO→pH and pH→DO
ccf1 <- get_ccf_df(avg_df$pH, avg_df$DO, lag.max = 8, "DO → Temp")
ccf2 <- get_ccf_df(avg_df$DO, avg_df$pH, lag.max = 8, "Temp → DO")

ccf_all <- bind_rows(ccf1, ccf2)

# 6) Plot both CCF curves together
ggplot(ccf_all, aes(x = lag, y = ccf, color = pair)) +
  geom_hline(yintercept = 0, linetype = "dashed") +
  geom_line(size = 1) +
  geom_point(size = 2) +
  scale_x_continuous(breaks = -8:8) +
  labs(
    title    = "Lead–Lag Correlations: Temp vs. DO",
    subtitle = "Negative lag = first variable leads second",
    x        = "Lag (quarters)",
    y        = "Cross-correlation",
    color    = "Direction"
  ) +
  theme_minimal()
