import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

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

G.add_edges_from([

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

# Type System

    # Overloading
    ('generic-functions', 'functions'),
    ('generic-functions', 'comptime-type-info'),
    ('operator-overloading', 'function-overloading'),
    ('dot-operator', 'operator-overloading'),
    ('variadic-arguments', 'function-overloading'),

    # Classes
    ('classes', 'simple-type-system'), # C-style structs
    ('generic-classes', 'classes'), # C++-style templates, but symbolic, not textual
    ('generic-classes', 'comptime-type-info'),
    ('interface-classes', 'classes'), # Java-style interfaces
    ('strict-generic-classes', 'generic-classes'), # Java-style generics
    ('strict-generic-classes', 'interface-classes'),
    ('inheriting-classes', 'interface-classes'), # C++ style inheritance
    ('inheriting-classes', 'type-casting'),
    ('multiple-inheriting-classes', 'inheriting-classes'),
    ('associated-class-types', 'classes'),
    ('associated-class-values', 'classes'),
    ('associated-interface-types', 'interface-classes'),
    ('associated-interface-values', 'interface-classes'),
    ('anonymous-classes', 'classes'),
    ('tuples', 'classes'),

    # Enumerations
    ('algebraic-enums', 'simple-enums'),
    ('generic-enums', 'algebraic-enums'),

    # Advanced
    # ...
    ('row-polymorphism', 'anonymous-classes'),
    ('row-polymorphism', 'static-type-checking'),

# Control Flow

    ('while-loops', 'loops'),
    ('iterables', 'interface-classes'),
    ('for-loops', 'iterables'),
    ('goto', 'loops'),
    ('pattern-matching', 'simple-enums'),
    ('advanced-pattern-matching', 'pattern-matching'),
    ('advanced-pattern-matching', 'algebraic-enums'),
    ('capturing-functions', 'functions'),

# Safety

    ('managed-types', 'classes'), # Garbage collection

# Type System

    # Dynamic Types
    ('any-type', 'dot-operator'),
    ('any-type', 'type-casting'),
    ('any-type', 'runtime-type-info'),
    ('managed-any-type', 'managed-types'),
    ('runtime-codegen', 'codegen-target'),
    ('runtime-codegen', 'runtime-type-info'),
    ('runtime-jit', 'runtime-codegen'),
    ('runtime-jit', 'native-codegen'),
    ('runtime-advanced-codegen', 'runtime-codegen'),
    ('runtime-advanced-codegen', 'interface-classes'),
    ('runtime-advanced-jit', 'runtime-advanced-codegen'),
    ('runtime-advanced-jit', 'native-codegen'),
    ('runtime-type-construction', 'runtime-codegen'),
    ('runtime-type-construction', 'classes'),
    ('runtime-type-modification', 'runtime-type-construction'),
    ('runtime-advanced-type-construction', 'runtime-type-construction'),
    ('runtime-advanced-type-construction', 'interface-classes'),
    ('runtime-advanced-type-modification', 'runtime-type-modification'),
    ('runtime-advanced-type-modification', 'interface-classes'),

    # Additional Information for compiler passes
    ('extended-pointer-types', 'simple-type-system'), # Const correctness, mutability
    ('extended-managed-types', 'managed-types'), # Const correctness n stuff for managed types

# Safety

    ('pointer-lifetime-analysis', 'extended-pointer-types'),
    ('pointer-lifetime-analysis', 'static-type-checking'),

# Compile-time execution

    ('comptime-conditionals', 'conditionals'),
    ('comp-directives', 'simple-type-system'),
    ('comptime-conditionals', 'comp-directives'),
    ('explicit-comptime-eval', 'comp-directives'),
    ('explicit-comptime-const-eval', 'comptime-type-info'),
    ('hygenic-macros', 'comptime-type-info'),
    ('hygenic-macros', 'scopes'),
    ('comptime-currying', 'comp-directives'),

# Control Flow

    ('for-loop-macro', 'for-loops'),
    ('for-loop-macro', 'hygenic-macros'),

# Metaprogramming

    ('comptime-metaprogram', 'comptime-type-info'),

# Optimization and Intent Declaration

    ('destructure-declaration', 'comp-directives'),
    ('function-annotations', 'extended-pointer-types'),

# Misc

])

pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=10)

plt.axis('off')
plt.show()
