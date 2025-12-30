import unreal

# Unreal subsystems
actor_subsys = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

# Outliner folder name
TARGET_FOLDER = "Blueprints"

# Get all actors in opened level
actors = actor_subsys.get_all_level_actors()

moved = 0

for actor in actors:
    cls = actor.get_class()
    bp = unreal.Blueprint.get_blueprint_from_class(cls)

    # if actor NOT blueprint-based → skip
    if not bp:
        continue

    # already inside folder → skip
    current_folder = actor.get_folder_path()
    if current_folder == TARGET_FOLDER:
        continue

    # place in folder
    actor.set_folder_path(TARGET_FOLDER)
    moved += 1
    unreal.log(f"[Move] {actor.get_name()} → {TARGET_FOLDER}")

unreal.log(f"✨ 완료: Blueprint 타입 Actor {moved}개가 아웃라이너 폴더 '{TARGET_FOLDER}' 로 정리되었습니다.")
