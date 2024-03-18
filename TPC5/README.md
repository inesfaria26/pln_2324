# pln_2324
Repositório Processamento de Linguagem Natural em Engenharia Biomédica

## TPC 5 - Tradução de conceitos de um livro médico

Objetivo - Apresentar o livro de conceitos médicos, sendo que os conceitos têm de ter uma descrição associada em português e o seu nome traduzido para inglês. 

No âmbito deste trabalho de casa, a tarefa consiste em desenvolver o código para a tradução de certos conceitos médicos que estão presentes num livro médico. Neste caso, optei por abordar o problema com o desenvolvimento de código que permita a tradução automática dos conceitos (presentes no documento json), sendo os mesmos apresentados na página html do livro, assim como a devida descrição em português.

### Desenvolvimento

O script Python foi desenvolvido para processar um arquivo JSON contendo termos médicos, bem como adicionar tooltips com descrições e traduções para esses termos em um texto HTML. Neste sentido, existe uma série de questõs que devem ser abordadas para que o script seja melhor compreendido:

1. Importação de Bibliotecas: Há a importação de bibliotecas que precisam ser usadas. Inclui o módulo json para manipulação de arquivos JSON, o módulo re para expressões regulares e a biblioteca "deep_translator" para tradução de palavras.

2. Carregamento de Dados: Com a utilização da função json.loads, o conteúdo de um arquivo JSON, neste caso do conceitos.json, é lido e carregado em uma estrutura de dados Python.

3. Configuração da blacklist: A blacklist é uma lista de palavras que não devem ser traduzidas ou incorporadas nos tooltips.

4. Função da Tradução: A biblioteca "deep_translator" é utilizada para criar uma instância do tradutor do Google. Usando-a, a função translate_word é configurada para traduzir uma palavra de português para inglês.

5. Função Etiquetador: A função etiquetador é configurada para processar todas as palavras presentes em texto HTML. Um tooltip inclui a descrição e a tradução do termo médico se a palavra estiver na lista de termos médicos e não estiver na blacklist. Caso contrário, o termo permanece inalterado.

6. Processamento do Texto HTML: As tags substituem as quebras de linha no texto HTML. Para além disso, a função etiquetador é utilizada para processar cada palavra do texto e, quando necessário, adicionar tooltips.

7. Processamento do Texto: O texto processado é escrito em um arquivo HTML chamado "livro.html".

### Conclusão

Assim, a abordagem da tradução automática não foi concluída com sucesso, dado que não foi concluído o objetivo pretendido - haver a tradução das palavras. Apesar de ter desenvolvido o script Python que permita a tradução das palavras que estejam na lista de conceitos médicos e que não estejam na blacklist. De notar que esta dificuldade deve ser superada em trabalhos futuros que seja necessário esta funcionalidade.