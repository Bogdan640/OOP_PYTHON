# import configparser
# import pathlib
# from src.repository.DisciplineRepo import DisciplineRepository, DisciplineTextRepo
# from src.repository.GradeRepo import GradeRepository, GradeTextRepository
# from src.repository.StudentRepo import StudentRepository, SdudentTextRepo
# from src.services.DisciplineServ import DisciplineService
# from src.services.GradeServ import GradeService
# from src.services.StudentServ import StudentServ
# from src.services.UndoServ import UndoService
# from src.ui.UI import UI
#
# config = configparser.ConfigParser()
# config.read('src/ui/settings.properties')
# config.sections()
#
# repository_type = config["repository"]["repositoryType"]
#
# discipline_repo_files = config['repository.files']['disciplines']
# student_repo_files = config['repository.files']['students']
# grade_repo_files = config['repository.files']['grades']
#
#
#
#
# if repository_type == 'inmemory':
#     discipline_repo = DisciplineRepository()
#     student_repo = StudentRepository()
#     grade_repo = GradeRepository()
#
# elif repository_type == 'textfiles' or repository_type == 'binaryfiles':
#     path = pathlib.Path(__file__).parent.parent.absolute().joinpath(discipline_repo_files)
#     discipline_repo = DisciplineTextRepo(path)
#     path = pathlib.Path(__file__).parent.parent.absolute().joinpath(student_repo_files)
#     student_repo = SdudentTextRepo(path)
#     path = pathlib.Path(__file__).parent.parent.absolute().joinpath(grade_repo_files)
#     grade_repo =GradeTextRepository(path)
#
#     discipline_repo.save_file()
#     student_repo.save_file()
#     grade_repo.save_file()
# else:
#     raise ValueError(f"Unsupported repository_type: {repository_type}")
#
#
# undo_service = UndoService()
# grade_service = GradeService(grade_repo, student_repo, discipline_repo, undo_service)
# discipline_service = DisciplineService(discipline_repo, undo_service, grade_service)
#
#
#
#
#
# student_service = StudentServ(student_repo, undo_service, grade_service)
#
# console = UI(student_service, discipline_service, grade_service, undo_service)
#
# console.run_program()
