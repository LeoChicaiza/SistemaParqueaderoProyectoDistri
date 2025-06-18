
using Microsoft.AspNetCore.Mvc;
using login_audit_service.Models;
using login_audit_service.Services;

namespace login_audit_service.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class AuditController : ControllerBase
    {
        private static readonly List<AuditRecord> AuditLogs = new();

        [HttpPost]
        public IActionResult LogAudit([FromBody] AuditRecord record)
        {
            AuditLogs.Add(record);
            return Ok(new { message = "Audit logged successfully" });
        }

        [HttpGet("{email}")]
        public IActionResult GetLogs(string email)
        {
            var logs = AuditLogs.Where(r => r.Email == email).ToList();
            if (!logs.Any()) return NotFound("No logs found for this email");
            return Ok(logs);
        }
    }
}
