# Udacity Full-Stack Developer (Projeto 3) - Análise de logs

Este projeto consiste numa ferramenta interna de relatórios (internal reporting tool) que usará informações do banco de dados para descobrir de que tipo de artigos os leitores do site gostam.

O banco de dados contém artigos de jornal, bem como o log do servidor web para o site. O log tem uma linha de banco de dados para cada vez que um leitor abre de uma página da web. Maiores detalhes do esquema do banco de dados em [db_schema.txt](db_schema.txt)

Usando essa informação, a ferramenta responde as seguintes perguntas sobre a atividade do usuário do site:

**1) Quais são os três artigos mais populares de todos os tempos?**

Quais artigos foram os mais acessados? Apresente esta informação como uma lista organizada com o artigo mais popular no topo.

Exemplo:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

**2) Quem são os autores de artigos mais populares de todos os tempos?**

Isto é, quando você organizar todos os artigos que cada autor escreveu, quais autores obtiveram mais views? Apresente esta informação como uma lista organizada com o autor mais popular no topo.

Exemplo:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Contribuidor anônimo — 1023 views

**3) Em quais dias mais de 1% das requisições resultaram em erros?**

A tabela de logs inclui um status de coluna que indica o código de status HTTP que o site de notícias enviou ao navegador do usuário (consulte novamente esta aula se você quiser rever a ideia dos códigos de status HTTP).

Exemplo:

July 29, 2016 — 2.5% errors

## Arquitetura:

A ferramenta é um arquivo Python com as queries SQL de cada pergunta definidas em um dicionário que, ao ser executado, faz a consulta na base de dados e gera o arquivo [analysis.txt](analysis.txt) com os resultados.

A ferramenta foi desenvolvida e testada numa máquina virtual (VM) disponibilizada pela Udacity para o curso que roda o sistema operacional Linux e já possui o Python e o banco de dados [PostgreSQL](https://www.postgresql.org/docs/9.4/static/app-psql.html) configurados.

## Instalação:

* Faça um clone do repositório
* Instale o [Git Bash](https://git-scm.com/downloads), [Vagrant](https://www.vagrantup.com/) e [VirtualBox](https://www.virtualbox.org/wiki/Downloads) (necessários para executar a VM). **OBS:** Em máquinas com Linux ou MacOS o Git Bash não é necessário
* Faça o [download](https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip) da máquina virtual da Udacity e descompacte o arquivo numa pasta local
* Abra o Git Bash (ou um terminal UNIX), acesse a pasta da VM e acesse a subpasta `vagrant`
* Execute os comandos abaixo para fazer a instalação e efetuar o login na VM (leva alguns minutos todo o processo)
    - `vagrant up`
    - `vagrant ssh`
* Faça o [download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) do arquivo de criação do banco de dados e descompacte o mesmo dentro da mesma subpasta `vagrant` que é compartilhada com a VM.
* Volte no terminal da VM e crie o banco de dados:
    - `cd /vagrant`
    - `psql -d news -f newsdata.sql`
* Por fim, coloque o arquivo `log_analysis.py` na mesma subpasta `vagrant` e faça a execução pelo terminal da VM. Será gerado o arquivo `analysis.txt` nesta mesma pasta:
    - `python log_analysis.py`

## Copyright

Esse projeto foi desenvolvido por Márcio Souza de Oliveira e tanto a VM quanto a base de dados foi disponibilizado pela Udacity.
