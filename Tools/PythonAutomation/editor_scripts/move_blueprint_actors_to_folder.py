import unreal

actor_subsys = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
TARGET_FOLDER = "Blueprints"

actors = actor_subsys.get_all_level_actors()
moved = 0

for actor in actors:
    cls = actor.get_class()
    class_name = cls.get_name()

    # 블루프린트 기반 Actor 판정방법 변경
    # 클래스명이 *_C 로 끝나면 Blueprint Generated Class 이므로 이동
    if not class_name.endswith("_C"):
        continue

    if actor.get_folder_path() == TARGET_FOLDER:
        continue

    actor.set_folder_path(TARGET_FOLDER)
    moved += 1
    unreal.log(f"[Move] {actor.get_name()} → {TARGET_FOLDER}")

unreal.log(f"완료: Blueprint Actor {moved}개 이동됨 → '{TARGET_FOLDER}'")
