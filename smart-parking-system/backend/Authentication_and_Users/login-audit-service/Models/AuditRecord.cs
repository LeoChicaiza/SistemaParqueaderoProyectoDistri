
namespace login_audit_service.Models
{
    public class AuditRecord
    {
        public string Email { get; set; }
        public string Action { get; set; }
        public DateTime Timestamp { get; set; }
    }
}
