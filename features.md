# Desired Language Features
Proggo-loggo intends, from the start, to be a bloated, hard-to-use language. It
will have an incredibly verbose, boilerplate-ridden syntax, large quantities of
completely useless cruft, and be essentially unusable in production. However,
it will still support the following features, organized into broad categories:

- Type System
  - Type checking
  - Type inference
  - Classes
  - Generics, both lax and strict
  - Polymorphism/Inheritance
  - Java-style Interfaces
  - Dynamic types

- Introspection
  - `Code` type
  - `Type` type
  - 

- Compile-time execution
  - Explicit constant evaluation
  - Meta program
  - Compile-time execution of functions
  - Miscellaneous compiler directives

- Misc
  - Native code output
  - Async-await

Additionally, its IR will be part of its public API, and will thus remain stable.
Note that this doesn't mean that its ABI will remain stable, at least for the forseeable
future.

