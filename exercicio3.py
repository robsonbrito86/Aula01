class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.__status = "disponível"  # Status privado

    def emprestar(self):
        if self.__status == "disponível":
            self.__status = "emprestado"
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")

    def devolver(self):
        if self.__status == "emprestado":
            self.__status = "disponível"
        else:
            print(f"O livro '{self.titulo}' já está disponível.")

    def status(self):
        return self.__status


# Classe Usuário (Base)
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.__historico = []  # Histórico protegido

    def adicionar_historico(self, livro):
        self.__historico.append(livro)

    def listar_historico(self):
        if self.__historico:
            print(f"Histórico de empréstimos de {self.nome}:")
            for livro in self.__historico:
                print(f" - {livro.titulo}")
        else:
            print(f"{self.nome} não possui histórico de empréstimos.")

    def limite_emprestimos(self):
        pass  # Método a ser sobrescrito pelas subclasses


# Classe Aluno (Herda de Usuário)
class Aluno(Usuario):
    def __init__(self, nome):
        super().__init__(nome)
        self.__limite = 3  # Limite de 3 empréstimos

    def limite_emprestimos(self):
        return self.__limite


# Classe Professor (Herda de Usuário)
class Professor(Usuario):
    def __init__(self, nome):
        super().__init__(nome)
        self.__limite = 5  # Limite de 5 empréstimos

    def limite_emprestimos(self):
        return self.__limite


# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def emprestar_livro(self, usuario, livro):
        if livro.status() == "disponível":
            if len(usuario._Usuario__historico) < usuario.limite_emprestimos():
                livro.emprestar()
                usuario.adicionar_historico(livro)
                print(f"O livro '{livro.titulo}' foi emprestado a {usuario.nome}.")
            else:
                print(f"{usuario.nome} atingiu o limite de empréstimos.")
        else:
            print(f"O livro '{livro.titulo}' não está disponível.")

    def devolver_livro(self, usuario, livro):
        if livro.status() == "emprestado":
            livro.devolver()
            print(f"O livro '{livro.titulo}' foi devolvido por {usuario.nome}.")
        else:
            print(f"O livro '{livro.titulo}' não foi emprestado.")

# Exemplo de uso:
# Criando livros
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 1899)

# Criando usuários
aluno1 = Aluno("Carlos")
professor1 = Professor("Ana")

# Criando a biblioteca e registrando livros e usuários
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.registrar_usuario(aluno1)
biblioteca.registrar_usuario(professor1)

# Emprestando livros
biblioteca.emprestar_livro(aluno1, livro1)
biblioteca.emprestar_livro(professor1, livro2)

# Listando histórico de usuários
aluno1.listar_historico()
professor1.listar_historico()

# Devolvendo livros
biblioteca.devolver_livro(aluno1, livro1)
biblioteca.devolver_livro(professor1, livro2)