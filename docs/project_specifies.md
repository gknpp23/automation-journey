# **Especificação de Projeto: Sistema de Monitoramento de Hardware com Persistência de Dados e Notificação Ativa**

---

### **1. Visão Geral e Objetivo**

O objetivo deste projeto é desenvolver um sistema modular em Python que monitore continuamente os recursos de hardware de uma máquina (GPU, CPU, Memória), persista os dados coletados em um banco de dados SQL local e envie alertas ativos para uma plataforma de comunicação (Telegram ou Discord) quando métricas específicas ultrapassarem limiares pré-configurados.

A aplicação deve ser robusta, bem documentada e seguir as melhores práticas de desenvolvimento de software, resultando em uma ferramenta funcional e de fácil manutenção.

### **2. Requisitos Técnicos Detalhados**

O sistema deve ser estruturado em módulos com responsabilidades claras.

#### **Módulo 1: Coletor de Dados (`collect.py`)**

Responsável por interagir com o sistema e o hardware para extrair as métricas.

* **Coleta de GPU:** Deve coletar métricas essenciais como nome, temperatura, utilização, uso de memória e consumo de energia.
* **Coleta de CPU:** Deve coletar o percentual de uso geral da CPU.
* **Coleta de Memória RAM:** Deve coletar o percentual de uso da memória RAM e a quantidade total utilizada (em MB).
* **Formato de Saída:** As funções de coleta devem retornar os dados em um formato estruturado (dicionário Python) para serem consumidos por outros módulos.

#### **Módulo 2: Persistência de Dados (`database.py`)**

Responsável por toda a interação com o banco de dados.

* **Banco de Dados:** Utilizar SQLite3, com o banco de dados sendo um único arquivo local.
* **Schema:** Definir e criar programaticamente as tabelas necessárias para armazenar as métricas, com tipos de dados apropriados (`TEXT`, `REAL`, etc.).
* **Operações:** Implementar funções para estabelecer a conexão e inserir novos registros de métricas de forma segura.

#### **Módulo 3: Sistema de Notificação (`alerts.py`)**

Componente desacoplado para o envio de alertas.

* **Integração:** O módulo deve ser capaz de enviar mensagens para a API do Telegram e/ou Discord.
* **Interface:** Deve expor uma função simples, como `send_alert(mensagem: str)`, que abstrai a complexidade da requisição HTTP.
* **Mensagens:** As mensagens de alerta devem ser claras, indicando qual limiar foi ultrapassado e o valor atual da métrica.

#### **Módulo 4: Orquestrador (`main.py`)**

O ponto de entrada e cérebro do sistema.

* **Configuração:** Permitir a fácil configuração de parâmetros como o intervalo de monitoramento e os limiares de alerta para CPU e RAM.
* **Loop Principal:** Implementar um loop contínuo que, a cada intervalo:
    1.  Chama o Módulo Coletor.
    2.  Chama o Módulo de Persistência para salvar os dados.
    3.  Avalia os dados e, se necessário, chama o Módulo de Notificação.
* **Tratamento de Erros:** Deve lidar com falhas comuns (ex: falha de rede ao enviar alerta) sem interromper a execução.

### **3. Requisitos Não-Funcionais**

Estes requisitos são cruciais para a qualidade e profissionalismo do projeto.

* **Código Limpo:** O código-fonte deve aderir estritamente ao guia de estilo **PEP 8**.
* **Segurança:** Nenhuma credencial (token de API) deve ser escrita diretamente no código. O uso de arquivos `.env` para carregar variáveis de ambiente é mandatório.
* **Gerenciamento de Dependências:** Todas as bibliotecas externas devem ser declaradas em um arquivo `requirements.txt`.
* **Documentação:** O projeto deve conter um arquivo `README.md` claro e completo, explicando o propósito do sistema, como configurá-lo e como executá-lo.
* **Controle de Versão:** O projeto deve ser versionado com Git, com um histórico de commits lógico e descritivo.

### **4. Escopo do Projeto Final**

O entregável final é um repositório Git completo e funcional, contendo todo o código-fonte, documentação (`README.md`) e arquivos de configuração (`requirements.txt`, `.gitignore`) necessários para a sua replicação e execução.