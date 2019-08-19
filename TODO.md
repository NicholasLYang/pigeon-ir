# TODO
- Semantics of SSA with scopes
  - How do mutable variables over loops work? Do scopes need parameters?
  - How do mutable variables that are conditionally mutated work? Do scopes need return values?
- Structure of passes
  - Should type inference be a compiler pass or a preprocessing step?
  - Should certain passes rebuild the IR as another structure? Do we need to rebuild
    the tree and/or use dynamic dispatch in order to statically check presuppositions
    of different passes? Or should we just make them implicit and use runtime checks
    during debugging?
