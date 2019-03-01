# CalculatePi
Calculate pi with a monte carlo method

To run:
```
python get_pi.py
```

Requires PyGame


# Issues

- The calculation starts from scratch for each iteration, which makes each iteration take more time than the last.
- There is a lot of jitter in the estimation, due to starting from scratch each time

# Task

Convert calculate_pi() to an iterator or generator, and modify the code accordingly


# Hints

- The "while True" loop can be replaced by an iterable
- The calculation needs some minor changes to work as an iterator/generator
- The "for _ in range(iterations)" loop may not be necessary
