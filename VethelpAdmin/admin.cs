using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;



//igualar os campos dos atributos da classe com os nomes dados no codigo python
// Id = id
public class User
{
    public int Id { get; set; }
    public string Nome { get; set; }
    public string Email { get; set; }
    public string Fone { get; set; }
    public string Senha { get; set; }

    // Construtor para inicializar os atributos
    public User(int id, string nome, string email, string fone, string senha)
    {
        Id = id;
        Nome = nome;
        Email = email;
        Fone = fone;
        Senha = senha;
    }

    // Método que vai retornar uma string representando o objeto
    public override string ToString()
    {
        return $"{Id} - {Nome} - {Email} - {Fone}";
    }
}

public class Users
{
    // Lista de objetos do tipo User
    private static List<User> objetos = new List<User>();
    private static string _filePath = "users.json"; // Nome do arquivo
    private static JsonSerializerSettings _jsonSettings = new JsonSerializerSettings
    {
        ContractResolver = new CamelCasePropertyNamesContractResolver() // Converte para camelCase (minúsculo)
    };


    // Método para inserir um novo usuário
    public static void Inserir(User obj)
    {
        Abrir(); // Abre o arquivo para carregar os dados
        // Calcula o ID do novo objeto, incrementando o ID máximo já existente
        int id = 0;
        foreach (var x in objetos)
        {
            if (x.Id > id) id = x.Id;
        }
        obj.Id = id + 1; // Atribui um novo ID ao objeto
        objetos.Add(obj); // Adiciona o novo objeto à lista
        Salvar(); // Salva a lista de usuários no arquivo JSON
    }

    // Método para listar todos os usuários
    public static List<User> Listar()
    {
        Abrir(); // Carrega a lista de objetos
        return objetos; // Retorna a lista de usuários
    }

    // Método para listar um usuário pelo ID
    public static User ListarId(int id)
    {
        Abrir(); // Carrega a lista de objetos
        return objetos.Find(x => x.Id == id); // Retorna o usuário com o ID correspondente
    }

    // Método para atualizar um usuário
    public static void Atualizar(User obj)
    {
        var usuario = ListarId(obj.Id); // Busca o usuário pelo ID
        if (usuario != null)
        {
            objetos.Remove(usuario); // Remove o usuário antigo
            objetos.Add(obj); // Adiciona o usuário atualizado
            Salvar(); // Salva as alterações no arquivo JSON
        }
    }

    // Método para excluir um usuário
    public static void Excluir(User obj)
    {
        var usuario = ListarId(obj.Id); // Busca o usuário pelo ID
        if (usuario != null)
        {
            objetos.Remove(usuario); // Remove o usuário
            Salvar(); // Salva as alterações no arquivo JSON
        }
    }

    // Método para salvar os dados no arquivo JSON
    private static void Salvar()
    {
        string json = JsonConvert.SerializeObject(objetos, Formatting.Indented, _jsonSettings); // Usa as configurações

        string basePath = Directory.GetCurrentDirectory(); // Pasta atual
        string vethelpPath = Path.Combine(basePath, "..", _filePath); // Volta um diretório

        File.WriteAllText(vethelpPath, json); // Escreve o JSON no arquivo no caminho correto
    
    }

    // Método para carregar os dados do arquivo JSON
    private static void Abrir()
    {
        objetos.Clear(); // Limpa a lista de objetos
        string basePath = Directory.GetCurrentDirectory();
        string vethelpPath = Path.Combine(basePath, "..", _filePath); // Volta um diretório

        if (File.Exists(vethelpPath)) // Verifica se o arquivo existe no caminho correto
        {
            string json = File.ReadAllText(vethelpPath); // Lê o arquivo JSON do caminho correto
            objetos = JsonConvert.DeserializeObject<List<User>>(json, _jsonSettings); // Usa as configurações na desserialização

        }
    }
}
