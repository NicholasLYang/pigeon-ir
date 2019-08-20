#![allow(dead_code)]

use std::collections::HashSet;

pub enum Type {
    Int64,
    Float64,
    None,
    // Eventually have actual types as well
}

/// Data associated with a variable in a scope. Includes type information, and
/// if the variable is named, also includes identifier that was used.
pub struct VarData<'a> {
    pub name: Option<&'a str>,
    pub type_info: Type,
}

pub enum Instruction {}

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

/// Table of variables. Symbol table with type information. Offset determines whether
/// we should skip this table and look at the calling table instead.
pub struct VarTable<'a> {
    pub data: Vec<VarData<'a>>,
    pub offset: usize,
}

/// Scope
pub struct Scope<'a> {
    vars: VarTable<'a>,
    capture: Option<HashSet<VarRef>>,
    // namespacing: NamespacePolicy,
    instructions: Vec<Instruction>,
}
