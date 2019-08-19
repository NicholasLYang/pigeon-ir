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
# - native code generation
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
    ('native-codegen', 'root'),

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
    ('classes', 'comptime-type-info'), # C-style structs
    ('generic-classes', 'classes'), # C++-style templates, but symbolic, not textual
    ('interfaces', 'classes'), # Java-style interfaces
    ('strict-generic-classes', 'generic-classes'), # Java-style generics
    ('strict-generic-classes', 'interfaces'),
    ('inheritance', 'interfaces'), # C++ style inheritance
    ('inheritance', 'type-casting'),
    ('associated-types', 'classes'),
    ('associated-values', 'classes'),
    ('associated-interface-types', 'interfaces'),
    ('associated-interface-values', 'interfaces'),
    ('anonymous-classes', 'classes'),
    ('tuples', 'classes'),

    # Enumerations
    ('algebraic-enums', 'simple-enums'),
    ('generic-enums', 'algebraic-enums'),

    # Dynamic Types
    ('any-type', 'dot-operator'),
    ('any-type', 'type-casting'),
    ('any-type', 'runtime-type-info'),
    ('runtime-codegen', 'native-codegen'),
    ('runtime-codegen', 'runtime-type-info'),
    ('runtime-jit', 'runtime-codegen'),
    ('runtime-advanced-codegen', 'runtime-codegen'),
    ('runtime-advanced-codegen', 'interfaces'),
    ('runtime-advanced-jit', 'runtime-advanced-codegen'),
    ('runtime-type-construction', 'runtime-codegen'),
    ('runtime-type-construction', 'classes'),
    ('runtime-type-modification', 'runtime-type-construction'),
    ('runtime-advanced-type-construction', 'runtime-type-construction'),
    ('runtime-advanced-type-construction', 'interfaces'),
    ('runtime-advanced-type-modification', 'runtime-type-modification'),
    ('runtime-advanced-type-modification', 'interfaces'),

    # Advanced
    # ...
    ('row-polymorphism', 'anonymous-classes'),
    ('row-polymorphism', 'static-type-checking'),

# Control Flow

    ('while-loops', 'loops'),
    ('iterables', 'interfaces'),
    ('for-loops', 'iterables'),
    ('goto', 'loops'),
    ('pattern-matching', 'simple-enums'),
    ('advanced-pattern-matching', 'pattern-matching'),
    ('advanced-pattern-matching', 'algebraic-enums'),
    ('capturing-functions', 'functions'),

# Safety

    ('managed-types', 'generic-classes'),
    ('garbage-collection', 'managed-types'),

# Type System

    ('extended-pointer-types', 'simple-type-system'),
    ('extended-managed-types', 'managed-types'),

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
