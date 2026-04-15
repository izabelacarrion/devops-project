# 🚀 DevOps Project - Cloud Native Application

Projeto prático de aplicação Python containerizada, com foco em boas práticas de DevOps, incluindo Docker, Kubernetes e CI/CD.

---

## 📌 Visão geral

A aplicação expõe endpoints HTTP para verificação de saúde e informações da aplicação:

- `/health` → verifica se a aplicação está viva  
- `/ready` → indica se a aplicação está pronta para receber tráfego  
- `/info` → retorna informações da aplicação (versão, ambiente e hostname)

Exemplo de resposta:

```json
{
  "status": "ok",
  "version": "1.0.0",
  "environment": "development",
  "hostname": "health-api-xxxx"
}
```
![alt text](/Assets/App.jpeg)

A aplicação roda na porta `8080` e utiliza a variável de ambiente `APP_ENV`.

---

## 🐍 Aplicação

Implementada em Python utilizando bibliotecas nativas (`http.server`).

### Executar localmente

```bash
export APP_ENV=development
python Projeto/App/app.py
```

---

## 🐳 Containerização (Docker)

A aplicação é containerizada utilizando uma imagem oficial do Python baseada em Alpine.

### Boas práticas adotadas

- uso de imagem base leve (`python:alpine`)
- execução como usuário não-root
- exposição da porta 8080
- suporte a variável de ambiente
- Scan de vulnerabilidades com Trivy no pipeline. Em uma das actions é possível identificar que o Trivy validou a versão do Alpine em uso pelo Dockerfile, o que posteriormente foi corrigido:
![alt text](/Assets/trivy.png)


## ☸️ Kubernetes

Os manifestos Kubernetes estão em `Projeto/K8s/`.

### Recursos criados

- Deployment  
- Service (ClusterIP)  
- Ingress  

### Configurações aplicadas

- 2 réplicas da aplicação  
- `livenessProbe` (`/health`)  
- `readinessProbe` (`/ready`)  
- definição de `resources` (CPU e memória)  
- uso de variável de ambiente (`APP_ENV`)  
- configuração de `securityContext`  

### Aplicação dos manifests

```bash
kubectl apply -f Projeto/K8s/
```

---

## ⚙️ CI/CD (GitHub Actions)

O pipeline automatiza:

- build da imagem Docker  
- scan de vulnerabilidades com Trivy  
- push da imagem para Docker Hub  
- criação de cluster Kubernetes com Kind  
- deploy da aplicação  
- validação dos endpoints (`/health`, `/ready`, `/info`)  

### Validação em Kubernetes

A aplicação é testada automaticamente em um cluster **Kind**, garantindo que:

- os manifests são aplicáveis  
- o deployment sobe corretamente  
- a aplicação responde via HTTP  

---

## 🔐 Segurança

O projeto adota práticas básicas de segurança:

- execução do container como usuário não-root  
- análise de vulnerabilidades com Trivy  
- falha da pipeline para vulnerabilidades críticas  
- uso de `securityContext` no Kubernetes  

---

## 🚧 Melhorias futuras

- versionamento dinâmico de imagens  
- uso de ConfigMap e Secret  
- observabilidade (logs e métricas)  
- deploy em cluster Kubernetes gerenciado (EKS)  

---

© 2026 - Desenvolvido por Izabela Carrion para fins de estudo em Cloud & DevOps.