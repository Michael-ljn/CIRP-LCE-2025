def lcaH2_2050(c_f_solar, c_f_wind, share, SEC):

  return (
  0.14413443664141418 + SEC * share * (33693.22925508887 / (1.7519999999999997e8 * c_f_wind) + 1980.8362095252687 / (1.7519999999999997e8 * c_f_wind) + 2828.892762022916 / (1.7519999999999997e8 * c_f_wind) + 510495.98780459305 / (1.7519999999999997e8 * c_f_wind) + 2.4690869910470077e-5 / (1.7519999999999997e8 * c_f_wind)) + SEC * (1 + -1 * share) * (268198.14689406 / (1.49796e8 * c_f_solar) + 8.508014316538438e-5 / (262800.0 * c_f_solar) + -0.00010959533884564421 / (262800.0 * c_f_solar))
)

if __name__ == "__main__":
  # Example usage
  c_f_solar = 1.0  # Example value for solar capacity factor
  c_f_wind = 1.0   # Example value for wind capacity factor
  share = 0.5      # Example share of renewable energy
  SEC = 1.0        # Example specific energy consumption

  result = lcaH2(c_f_solar, c_f_wind, share, SEC)
  print(f"LCA result: {result}")