#[allow(dead_code)]

// Eventually have actual types as well
pub enum Type {
    /// Integral value
    Int64,
    /// Floating point value
    Float64,
    /// The type isn't known to the compiler yet
    None,
    PointerTo(Box<Type>),
    PointerToPointer {
        indirections: u8,
        pointer_to: Box<Type>,
    },
}

pub enum Instruction {
    Add,
}

/// Data associated with a variable in a scope. Includes type information, and
/// if the variable is named, also includes identifier that was used.
pub struct VarData<'a> {
    name: Option<&'a str>,
    type_info: Type,
}

/// Reference to a variable.
#[derive(Hash, PartialEq, Eq)]
pub struct VarRef {
    id: u32,      // Index into the VarTable
    version: u32, // ID for name generation, to maintain SSA form
}

impl PartialOrd for VarRef {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        use std::cmp::Ordering;
        let cmp = self.id.cmp(&other.id);
        let ret = if cmp == Ordering::Equal {
            self.version.cmp(&other.version)
        } else {
            cmp
        };
        Some(ret)
    }
}
