from dependency_injector import containers, providers
from domain.file.service import FileService
from domain.file.repository import FileRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["domain"],
        modules=["main"],
    )
    file_repository: FileRepository = providers.Singleton(FileRepository)
    file_service: FileService = providers.Singleton(FileService, file_repository)
