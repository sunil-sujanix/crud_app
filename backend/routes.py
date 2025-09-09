from flask import Blueprint, jsonify, request
from models import db, Tasks

routes_bp = Blueprint("routes", __name__)  

# ---- helpers ----
def task_to_dict(t: Tasks):
    return {
        "id": t.id,
        "title": t.title,
        "completed": bool(t.completed),
        "created_at": t.created_at.isoformat() if t.created_at else None,
    }



# List all (optionally ?completed=true/false)
@routes_bp.get("/tasks")
def list_tasks():
    q = Tasks.query
    completed = request.args.get("completed")
    if completed is not None:
        if completed.lower() in ("true", "1", "yes", "y"):
            q = q.filter_by(completed=True)
        elif completed.lower() in ("false", "0", "no", "n"):
            q = q.filter_by(completed=False)
    tasks = q.order_by(Tasks.id.desc()).all()
    return jsonify({"message": "ok", "data": [task_to_dict(t) for t in tasks]}), 200

# Get one
@routes_bp.get("/tasks/<int:task_id>")
def get_task(task_id: int):
    t = Tasks.query.get(task_id)
    if not t:
        return jsonify({"message": "not found"}), 404
    return jsonify(task_to_dict(t)), 200

# Create
@routes_bp.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"message": "title is required"}), 400
    completed = bool(data.get("completed", False))

    t = Tasks(title=title, completed=completed)
    db.session.add(t)
    db.session.commit()
    return jsonify(task_to_dict(t)), 201

# Full update (PUT)
@routes_bp.put("/tasks/<int:task_id>")
def update_task(task_id: int):
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"message": "title is required"}), 400
    completed = bool(data.get("completed", False))

    t = Tasks.query.get(task_id)
    if not t:
        return jsonify({"message": "not found"}), 404

    t.title = title
    t.completed = completed
    db.session.commit()
    return jsonify(task_to_dict(t)), 200

# Partial update (PATCH)
@routes_bp.patch("/tasks/<int:task_id>")
def patch_task(task_id: int):
    data = request.get_json(silent=True) or {}
    t = Tasks.query.get(task_id)
    if not t:
        return jsonify({"message": "not found"}), 404

    if "title" in data:
        new_title = (data.get("title") or "").strip()
        if not new_title:
            return jsonify({"message": "title cannot be empty"}), 400
        t.title = new_title
    if "completed" in data:
        t.completed = bool(data["completed"])

    db.session.commit()
    return jsonify(task_to_dict(t)), 200

# Delete
@routes_bp.delete("/tasks/<int:task_id>")
def delete_task(task_id: int):
    t = Tasks.query.get(task_id)
    if not t:
        return jsonify({"message": "not found"}), 404
    db.session.delete(t)
    db.session.commit()
    return jsonify({"message": "deleted"}), 200
