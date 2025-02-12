using System;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;



//igualar os campos dos atributos da classe com os nomes dados no codigo python
// Id = id
public class ServiceItem
{
    public int Id { get; set; }
    public int Qtd { get; set; }
    public double Price { get; set; } 
    public int Service_id { get; set; }
    public int Product_id { get; set; }
    public int Procedure_id { get; set; }

    // Construtor para inicializar os atributos id, qtd, preco, service_id, product_id, procedure_id
    public ServiceItem(int id, int qtd, double price, int service_id, int product_id, int procedure_id)
    {
        Id = id;
        Qtd = qtd;
        Price = price;
        Service_id = service_id;
        Product_id = product_id;
        Procedure_id = procedure_id;
    }

    // Método que vai retornar uma string representando o objeto
    public override string ToString()
    {
        return $"{Id} - {Qtd} - {Price} - {Service_id} - {Product_id} - {Procedure_id}";
    }
}

public class ServiceItems
{
    // Lista de objetos do tipo ServiceItem
    private static List<ServiceItem> objetos = new List<ServiceItem>();
    private static string _filePath = "service_items.json"; // Nome do arquivo
    private static JsonSerializerSettings _jsonSettings = new JsonSerializerSettings
    {
        ContractResolver = new CamelCasePropertyNamesContractResolver() // Converte para camelCase (minúsculo)
    };


    // Método para inserir um novo usuário
    public static void Inserir(ServiceItem obj)
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
    public static List<ServiceItem> Listar()
    {
        Abrir(); // Carrega a lista de objetos
        return objetos; // Retorna a lista de usuários
    }

    // Método para listar um usuário pelo ID
    public static ServiceItem ListarId(int id)
    {
        Abrir(); // Carrega a lista de objetos
        return objetos.Find(x => x.Id == id); // Retorna o usuário com o ID correspondente
    }

    // Método para atualizar um usuário
    public static void Atualizar(ServiceItem obj)
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
    public static void Excluir(ServiceItem obj)
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
            objetos = JsonConvert.DeserializeObject<List<ServiceItem>>(json, _jsonSettings); // Usa as configurações na desserialização

        }
    }
}
