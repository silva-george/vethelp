using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;



//igualar os campos dos atributos da classe com os nomes dados no codigo python
// Id = id
public class Invoice
{
    public int Id { get; set; }
    public int Recepcionist_id { get; set; }
    public int Vet_id { get; set; }
    public int Animal_id { get; set; }
    public int Procedure_id { get; set; }
    public int Product_id { get; set; }
    public string Description { get; set; }
    public string Date { get; set; }
    public int Status { get; set; }

    // Construtor para inicializar os atributos
    public Invoice(int id, int recepcionist_id, int vet_id, int animal_id, int procedure_id, int product_id, string description, string date, int status)
    {
        Id = id;
        Recepcionist_id = recepcionist_id;
        Vet_id = vet_id;
        Animal_id = animal_id;
        Procedure_id = procedure_id;
        Product_id = product_id;
        Description = description;
        Date = date;
        Status = status;
    }

    // Método que vai retornar uma string representando o objeto
    public override string ToString()
    {
        return $"{Id} - {Recepcionist_id} - {Vet_id} - {Animal_id} - {Procedure_id} - {Product_id} - {Description} - {Date} - {Status}";
    }
}

public class Invoices
{
    // Lista de objetos do tipo Invoice
    private static List<Invoice> objetos = new List<Invoice>();
    private static string _filePath = "invoices.json"; // Nome do arquivo
    private static JsonSerializerSettings _jsonSettings = new JsonSerializerSettings
    {
        ContractResolver = new CamelCasePropertyNamesContractResolver() // Converte para camelCase (minúsculo)
    };


    // Método para inserir um novo usuário
    public static void Inserir(Invoice obj)
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
    public static List<Invoice> Listar()
    {
        Abrir(); // Carrega a lista de objetos
        return objetos; // Retorna a lista de usuários
    }

    // Método para listar um usuário pelo ID
    public static Invoice ListarId(int id)
    {
        Abrir(); // Carrega a lista de objetos
        return objetos.Find(x => x.Id == id); // Retorna o usuário com o ID correspondente
    }

    // Método para atualizar um usuário
    public static void Atualizar(Invoice obj)
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
    public static void Excluir(Invoice obj)
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
            objetos = JsonConvert.DeserializeObject<List<Invoice>>(json, _jsonSettings); // Usa as configurações na desserialização

        }
    }
}
