import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Required features:
# - Simple type system: Signed and unsigned integers, floating points, characters, pointers, arrays, dynamic arrays
# - Globals
# - Functions
# - Main
# - print and input
# - Conditionals
# - loops
# - Code generation target
# - Scopes/Namspaces

# Features included by default if available:
# - Atomics
# - Locks
# - Threading

# A feature can only alter the semantics of its ancestors
# Featureset must be have bounds known at compile-time

edges = [

# Features are things that need to be enabled to be in the language at all. They're
# orthogonal to "implicit behavior", which can be customized to the extent that
# the intended behavior conforms to the available features

# Root

    ('simple-type-system', 'root'),
    ('loops', 'root'),
    ('conditionals', 'root'),
    ('functions', 'root'),
    ('scopes', 'root'),
    ('codegen-target', 'root'),
    ('native-codegen', 'codegen-target'),

# Type System
    # Simple type system
    ('zero-sized-types', 'simple-type-system'),
    ('static-type-checking', 'simple-type-system'),
    ('type-inference', 'static-type-checking'),
    ('simple-enums', 'simple-type-system'),
    ('type-casting', 'simple-type-system'),
    ('function-overloading', 'functions'),
    ('oop-methods', 'functions'), # this pointer n all that jazz
    ('value-matching', 'simple-type-system'), # Switch statements
    ('associative-scopes', 'scopes'),
    ('lazy-constant-evaluation', 'associative-scopes'),

# Introspection
    ('comptime-type-info', 'static-type-checking'),
    ('runtime-type-info', 'simple-type-system'), # `Type` object
    ('runtime-namespace-info', 'runtime-type-info'), # Information about namespaces
    ('comptime-keyword-argument-hashtables', 'type-casting'), # Python-like arg dicts
    ('comptime-keyword-argument-hashtables', 'comptime-type-info'),
    ('comptime-positional-argument-arrays', 'type-casting'), # Python-like arg lists
    ('comptime-positional-argument-arrays', 'comptime-type-info'),
    # ('positional-argument-arrays', 'runtime-type-info'),
    # ('keyword-argument-hashtables', 'runtime-type-info'),

# Type System

    # Overloading
    ('generic-functions', 'functions'),
    ('generic-functions', 'comptime-type-info'),
    ('operator-overloading', 'function-overloading'),
    ('dot-operator', 'operator-overloading'),
    ('variadic-arguments', 'function-overloading'),

    # Classes
    ('static-classes', 'static-type-checking'), # C-style structs
    ('generic-classes', 'static-classes'), # C++-style templates, but symbolic, not textual
    ('generic-classes', 'comptime-type-info'),
    ('interface-classes', 'static-classes'), # Java-style interfaces
    ('strict-generic-classes', 'generic-classes'), # Java-style generics
    ('strict-generic-classes', 'interface-classes'),
    ('inheriting-classes', 'interface-classes'), # C++ style inheritance
    ('inheriting-classes', 'type-casting'),
    ('multiple-inheriting-classes', 'inheriting-classes'),

    # Type-checked values, like static values in Java
    ('static-associated-class-types', 'static-classes'),
    ('static-associated-class-values', 'static-classes'),

    # Associated trait types in Rust
    ('associated-interface-types', 'interface-classes'),
    ('associated-interface-values', 'interface-classes'),

    ('anonymous-classes', 'static-classes'),
    ('tuples', 'static-classes'),

    # Enumerations
    ('algebraic-enums', 'simple-enums'),
    ('generic-enums', 'algebraic-enums'),

    # Advanced
    ('row-polymorphism', 'anonymous-classes'),
    ('row-polymorphism', 'static-type-checking'),

        # native RAII-like support

# Control Flow

    ('iterables', 'interface-classes'),
    ('for-loops', 'iterables'),
    ('goto', 'loops'),
    ('pattern-matching', 'simple-enums'),
    ('advanced-pattern-matching', 'pattern-matching'), # Switch statements
    ('advanced-pattern-matching', 'algebraic-enums'), # Rust-like matching
    ('capturing-functions', 'functions'), # Lambdas

# Safety

    ('managed-types', 'static-classes'), # Garbage collection

# Type System

    # Dynamic Types
    ('any-type', 'dot-operator'), # Simple 'any' type, using type info generated in the binary
    ('any-type', 'type-casting'),
    ('any-type', 'comptime-type-info'),
    ('managed-any-type', 'any-type'), # Any type with garbage collection
    ('managed-any-type', 'managed-types'),
    ('managed-any-type', 'runtime-type-info'),

# Runtime flexibility
    ('dynamic-classes', 'any-type'),
    ('runtime-codegen', 'codegen-target'), # Building simple functions runtime types
    ('runtime-codegen', 'runtime-type-info'),
    ('runtime-code-modification', 'runtime-codegen'), # Things like altering functions
    ('runtime-jit', 'runtime-codegen'),
    ('runtime-jit', 'native-codegen'),

    # Constructing types at runtime
    ('static-runtime-type-construction', 'runtime-codegen'),
    ('static-runtime-type-construction', 'static-classes'),
    ('static-runtime-type-modification', 'static-runtime-type-construction'),

    # Constructing types at runtime
    ('dynamic-runtime-type-construction', 'runtime-codegen'),
    ('dynamic-runtime-type-construction', 'dynamic-classes'),
    ('dynamic-runtime-type-modification', 'dynamic-runtime-type-construction'),

    # Additional Information for compiler passes
    ('extended-pointer-types', 'simple-type-system'), # Const correctness, mutability
    ('extended-managed-types', 'managed-types'), # Const correctness n stuff for managed types

    # Python-like namespaces
    ('dynamic-namespaces', 'runtime-namespace-info'),

# Safety

    ('pointer-lifetime-analysis', 'extended-pointer-types'),
    ('pointer-lifetime-analysis', 'static-type-checking'),

# Compile-time execution

    ('comp-directives', 'simple-type-system'), # Compiler directives
    ('comptime-conditionals', 'conditionals'), # Static if
    ('comptime-conditionals', 'comp-directives'),
    ('explicit-comptime-eval', 'comp-directives'), # Compile-time evaluation
    ('explicit-comptime-const-eval', 'comptime-type-info'), # Compile-time constant evaluation
    ('hygenic-macros', 'comptime-type-info'),
    ('hygenic-macros', 'scopes'),
    ('comptime-currying', 'comp-directives'), # Compile-time function currying

# Control Flow

    ('for-loop-macro', 'for-loops'),
    ('for-loop-macro', 'hygenic-macros'),

# Metaprogramming

    ('comptime-metaprogram', 'comptime-type-info'),

# Optimization and Intent Declaration

    ('destructure-declaration', 'comp-directives'), # If this object isn't passed out of the current scope, destructure it into its fields
    ('function-annotations', 'extended-pointer-types'), # Extra metadata about function behavior

# Misc

]

G.add_edges_from([(e[1], e[0]) for e in edges])

pos=nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')

nx.draw_networkx_nodes(G, pos, node_size=5)
nx.draw_networkx_edges(G, pos, width=.5, node_size=5)
text = nx.draw_networkx_labels(G, pos, font_size=8)

for _,t in text.items():
    t.set_rotation(30)

plt.axis('off')
plt.show()
