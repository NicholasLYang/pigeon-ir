# Pigeon IR
Intermediate representation for the Pigeon compiler.

## Optimization
Optimization passes of Pigeon IR can be intrusive or non-intrusive:

- **Intrusive optimizations** make changes to the source code, potentially altering
  the semantics to the program, and include those changes in any debug information.
- **Non-intrusive optimizations** only change code in ways that preserves the
  semantics of the original program in its entirety. This allows for things like
  constant propogation on singular expressions, but doesn't allow much more than that.


