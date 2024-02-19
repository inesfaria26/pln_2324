# pln_2324
Repositório Processamento de Linguagem Natural em Engenharia Biomédica

TP1 - Procura de anagramas num texto (CIH Bilingual Medical Glossary)

Objetivo - Num documento de texto, verificar quais são as palavras que são anagramas entre elas.

No âmbito deste trabalho de casa, a tarefa consiste em analisar um documento de texto com o intuito de identificar palavras que são anagramas entre si. Os anagramas são palavras ou frases formadas pela reorganização das letras de outra palavra ou frase, utilizando todas as letras originais exatamente uma vez. 

A implementação envolverá a criação de uma função que, ao percorrer o documento, identificará e registrará as palavras anagramas, possibilitando uma análise mais aprofundada das relações entre termos presentes no texto após a obtenção dos resultados. Para além disso, foi desenvolvido uma função auxiliar para facilitar a identificação das palavras que são, de facto, anagramas. Este processo proporcionará uma compreensão mais refinada da estrutura linguística presente no documento, contribuindo para uma análise mais abrangente e precisa do conteúdo textual.

## Função anagrams

A função anagrams trata-se da função auxiliar que deteta se duas strings são anagramas uma da outra. Assim, o procedimento inicia-se com a conversão dos caracteres de duas strings para minúsculas, seguida da divisão em palavras. Posteriormente, as letras de cada palavra são ordenadas individualmente, considerando os espaços entre elas. A função retorna verdadeiro se as strings ordenadas resultantes são idênticas, indicando a presença de anagramas.


## Função verificarAnagrama

A função verificarAnagrama trata-se da função principal que vai proceder à análise do texto e à identificação das palavras que são anagramas. A função em si realiza uma comparação entre todas as combinações únicas, identificando e registando os pares de anagramas entre si. A lista areAnagrams armazena os pares que atendem essa condição.  

## Conclusão

A identificação e análise de anagramas não apenas enriquece a análise linguística, mas também tem aplicações práticas em diversos campos, como processamento de linguagem natural, criptografia e análise de dados textuais extensos. Assim, o trabalho desenvolvido proporciona uma visão detalhada das interconexões entre palavras, promovendo uma abordagem mais refinada e completa na interpretação de conjuntos de tokens.
