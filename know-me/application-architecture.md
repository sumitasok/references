### logging

---
### Resource Actions
#### Deletion
- Soft Delete - never hard delete.
- Create a module that handles soft delete including logging who deleted
- dont allow deletion if deleted_by is NULL.
- embed the module into the respource that supports deletion.
- deletable
  - deleted_at
  - deleted_by
  - deletion_flow

#### Updation/Creation
- Audit Trail
- updated_by maintained in audit trail -- mandatory, update fails in case of missing.
- ruby gems like paper_trail.
- If delayed jobs updating a resource -- the person who queued the delayed job should be logged.
- __Flow Capture__:
  - In case, a scheduled job updated the object, log which flow did that.
  - maintain which flow created the resource. this has a lot of value in analytics and debugging.
