#![allow(dead_code)]
use std::collections::HashSet;

pub enum Type {
    Int64,
    Float64,
    None,
    // Eventually have actual types as well
}

pub struct VarData<'a> {
    pub name: &'a str,
    pub type_info: Type,
}

pub enum Instruction {}

#[derive(Hash)]
pub struct VarRef {
    id: u32,   // The index into the
    vers: u32, // The version of the variable
}

/// Table of variables
pub struct VarTable<'a> {
    pub data: Vec<VarData<'a>>,
    pub offset: usize,
}

/// Scope
pub struct Scope<'a> {
    vars: VarTable<'a>,
    capture: Option<HashSet<VarRef>>,
    instructions: Vec<Instruction>,
}
