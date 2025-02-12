using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;



//igualar os campos dos atributos da classe com os nomes dados no codigo python
// Id = id
public class Receptionist
{
    public int UserId { get; set; }
    public int Id { get; set; }
    public string Cpf { get; set; }

    // Construtor para inicializar os atributos
    public Receptionist(int user_id, int id, string cpf)
    {
        UserId = user_id;
        Id = id;
        Cpf = cpf;
    }

    // Método que vai retornar uma string representando o objeto
    public override string ToString()
    {
        return $"{Id} - {Cpf}";
    }
}

public class Receptionists
{
    // Lista de objetos do tipo Receptionist
    private static List<Receptionist> objetos = new List<Receptionist>();
    private static string _filePath = "receptionists.json"; // Nome do arquivo
    private static JsonSerializerSettings _jsonSettings = new JsonSerializerSettings
    {
        ContractResolver = new CamelCasePropertyNamesContractResolver() // Converte para camelCase (minúsculo)
    };


    // Método para inserir um novo usuário
    public static void Inserir(Receptionist obj)
    {
        Abrir(); // Abre o arquivo para carregar os dados
        // Calcula o ID do novo objeto, incrementando o ID máximo já existente
        objetos.Add(obj); // Adiciona o novo objeto à lista
        Salvar(); // Salva a lista de usuários no arquivo JSON
    }

    // Método para listar todos os usuários
    public static List<Receptionist> Listar()
    {
        Abrir(); // Carrega a lista de objetos
        return objetos; // Retorna a lista de usuários
    }

    // Método para listar um usuário pelo ID
    public static Receptionist ListarId(int id)
    {
        Abrir(); // Carrega a lista de objetos
        return objetos.Find(x => x.Id == id); // Retorna o usuário com o ID correspondente
    }

    // Método para atualizar um usuário
    public static void Atualizar(Receptionist obj)
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
    public static void Excluir(Receptionist obj)
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
            objetos = JsonConvert.DeserializeObject<List<Receptionist>>(json, _jsonSettings); // Usa as configurações na desserialização

        }
    }
}
