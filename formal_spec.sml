signature MCP_SOLVER = sig
    val audit : int -> string
end;

structure MCPSolver : MCP_SOLVER = struct
    fun audit s =
        if s < 0 then "ENTROPY_DETECTED: NEGATIVE_STATE"
        else if s > 100 then "ENTROPY_DETECTED: OVERFLOW_STATE"
        else "LOGIC_PURITY_VERIFIED"
end;

val _ = print (MCPSolver.audit 50 ^ "\n");
val _ = OS.Process.exit OS.Process.success;
