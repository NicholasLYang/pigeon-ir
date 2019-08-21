#![allow(dead_code)]

use crate::ir_data::*;

/// Table of variables. Symbol table with type information. Offset determines whether
/// we should skip this table and look at the calling table instead.
pub struct VarTable<'a> {
    data: Vec<VarData<'a>>,
    offset: usize,
}

/// Scope
pub struct Scope<'a> {
    vars: VarTable<'a>,
    instructions: Vec<Instruction>,
}
