using System;
using System.Collections.Generic;

public class Program
{
    public static void Main(string[] args)
    {
        // Criação de novos objetos User
        var c1 = new User(0, "João", "j@j.com", "123", "123");
        Users.Inserir(c1); // Insere o primeiro usuário

        var c2 = new User(0, "João2", "j2@j.com", "123", "123");
        Users.Inserir(c2); // Insere o segundo usuário

        
        // Criação de novos objetos Vet
        var vet1 = new Vet(c1.Id, c1.Id, "cpf 123", "crm 123");
        Vets.Inserir(vet1);

        var vet2 = new Vet(c2.Id, c2.Id, "cpf 1234", "crm 1234");
        Vets.Inserir(vet2);

        // Listar todos os usuários
        var lista = Users.Listar();
        Console.WriteLine("Users no arquivo users.json:");
        foreach (var user in lista)
        {
            Console.WriteLine(user); // Chama o método ToString() da classe User
        }

        // listar todos os veterinários
        var vets = Vets.Listar();
        Console.WriteLine("Vets no arquivo vets.json:");
        foreach (var vet in vets)
        {
            Console.WriteLine(vet); // Chama o método ToString() da classe Vet
        }

        // Listar um usuário pelo ID
        int idParaBuscar = 2; // ID do segundo usuário
        var usuarioEncontrado = Users.ListarId(idParaBuscar);
        if (usuarioEncontrado != null)
        {
            Console.WriteLine($"\nUsuário com ID {idParaBuscar}:");
            Console.WriteLine(usuarioEncontrado);
        }
        else
        {
            Console.WriteLine($"\nNenhum usuário encontrado com ID {idParaBuscar}.");
        }

        // Atualizar um usuário
        if (usuarioEncontrado != null)
        {
            usuarioEncontrado.Nome = "João Atualizado";
            Users.Atualizar(usuarioEncontrado);
            Console.WriteLine("\nUsuário atualizado:");
            Console.WriteLine(usuarioEncontrado);
        }

        // Excluir um usuário
        int idParaExcluir = 1; // ID do primeiro usuário
        var usuarioParaExcluir = Users.ListarId(idParaExcluir);
        if (usuarioParaExcluir != null)
        {
            Users.Excluir(usuarioParaExcluir);
            if (Vets.ListarId(idParaExcluir) != null)
            {
                Vets.Excluir(Vets.ListarId(idParaExcluir));
            }
            Console.WriteLine($"\nUsuário com ID {idParaExcluir} excluído.");
        }

        // Listar todos os usuários após a exclusão
        lista = Users.Listar();
        Console.WriteLine("\nUsers no arquivo users.json após a exclusão:");
        foreach (var user in lista)
        {
            Console.WriteLine(user);
        }

        // Listar todos os veterinários depois da exclusão
        vets = Vets.Listar();
        Console.WriteLine("\nVets no arquivo vets.json depois da exclusão:");
        foreach (var vet in vets)
        {
            Console.WriteLine(vet);
        }
    }
}