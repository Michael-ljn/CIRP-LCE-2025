def lcaH2_2030(c_f_solar, c_f_wind, share, SEC):

  return (
  0.2657991919699085 + SEC * (1 + -1 * share) * (-0.00015566997436970256 / (262800.0 * c_f_solar) + 543076.3144180699 / (1.49796e8 * c_f_solar) + 0.00022847899562587412 / (262800.0 * c_f_solar)) + SEC * share * (59626.90138524987 / (1.7519999999999997e8 * c_f_wind) + 3.2622785404936014e-5 / (1.7519999999999997e8 * c_f_wind) + 2225.066250763144 / (1.7519999999999997e8 * c_f_wind) + 2834.0145098614917 / (1.7519999999999997e8 * c_f_wind) + 731523.949769357 / (1.7519999999999997e8 * c_f_wind))
)

if __name__ == "__main__":
  # Example usage
  c_f_solar = 1.0  # Example value for solar capacity factor
  c_f_wind = 1.0   # Example value for wind capacity factor
  share = 0.5      # Example share of renewable energy
  SEC = 1.0        # Example specific energy consumption

  result = lcaH2(c_f_solar, c_f_wind, share, SEC)
  print(f"LCA result: {result}")