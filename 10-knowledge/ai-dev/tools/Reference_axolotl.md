---
title: axolotl (Reference)
tags:
  - Reference
  - axolotl
  - Auto_Absorbed
---

# axolotl (OpenAccess-AI-Collective/axolotl)

<p align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/887513285d98132142bf5db2a74eb5e0928787f1/image/axolotl_logo_digital_white.svg">
        <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/887513285d98132142bf5db2a74eb5e0928787f1/image/axolotl_logo_digital_black.svg">
        <img alt="Axolotl" src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/887513285d98132142bf5db2a74eb5e0928787f1/image/axolotl_logo_digital_black.svg" width="400" height="104" style="max-width: 100%;">
    </picture>
</p>
  <p align="center">
      <strong>A Free and Open Source LLM Fine-tuning Framework</strong><br>
  </p>

<p align="center">
    <img src="https://img.shields.io/github/license/axolotl-ai-cloud/axolotl.svg?color=blue" alt="GitHub License">
    <img src="https://github.com/axolotl-ai-cloud/axolotl/actions/workflows/tests.yml/badge.svg" alt="tests">
    <a href="https://codecov.io/gh/axolotl-ai-cloud/axolotl"><img src="https://codecov.io/gh/axolotl-ai-cloud/axolotl/branch/main/graph/badge.svg" alt="codecov"></a>
    <a href="https://github.com/axolotl-ai-cloud/axolotl/releases"><img src="https://img.shields.io/github/release/axolotl-ai-cloud/axolotl.svg" alt="Releases"></a>
    <br/>
    <a href="https://github.com/axolotl-ai-cloud/axolotl/graphs/contributors"><img src="https://img.shields.io/github/contributors-anon/axolotl-ai-cloud/axolotl?color=yellow&style=flat-square" alt="contributors" style="height: 20px;"></a>
    <img src="https://img.shields.io/github/stars/axolotl-ai-cloud/axolotl" alt="GitHub Repo stars">
    <br/>
    <a href="https://discord.com/invite/HhrNrHJPRb"><img src="https://img.shields.io/badge/discord-7289da.svg?style=flat-square&logo=discord" alt="discord" style="height: 20px;"></a>
    <a href="https://twitter.com/axolotl_ai"><img src="https://img.shields.io/twitter/follow/axolotl_ai?style=social" alt="twitter" style="height: 20px;"></a>
    <a href="https://colab.research.google.com/github/axolotl-ai-cloud/axolotl/blob/main/examples/colab-notebooks/colab-axolotl-example.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google-colab" style="height: 20px;"></a>
    <br/>
    <img src="https://github.com/axolotl-ai-cloud/axolotl/actions/workflows/tests-nightly.yml/badge.svg" alt="tests-nightly">
    <img src="https://github.com/axolotl-ai-cloud/axolotl/actions/workflows/multi-gpu-e2e.yml/badge.svg" alt="multigpu-semi-weekly tests">
</p>


## 🎉 Latest Updates

- 2026/03:
  - New model support has been added in Axolotl for [Mistral Small 4](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/mistral4), [Qwen3.5, Qwen3.5 MoE](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/qwen3.5), [GLM-4.7-Flash](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/glm47-flash), [GLM-4.6V](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/glm46v), and [GLM-4.5-Air](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/glm45).
  - [MoE expert quantization](https://docs.axolotl.ai/docs/expert_quantization.html) support (via `quantize_moe_experts: true`) greatly reduces VRAM when training MoE models (FSDP2 compat).
- 2026/02:
  - [ScatterMoE LoRA](https://github.com/axolotl-ai-cloud/axolotl/pull/3410) support. LoRA fine-tuning directly on MoE expert weights using custom Triton kernels.
  - Axolotl now has support for [SageAttention](https://github.com/axolotl-ai-cloud/axolotl/pull/2823) and [GDPO](https://github.com/axolotl-ai-cloud/axolotl/pull/3353) (Generalized DPO).
- 2026/01:
  - New integration for [EAFT](https://github.com/axolotl-ai-cloud/axolotl/pull/3366) (Entropy-Aware Focal Training), weights loss by entropy of the top-k logit distribution, and [Scalable Softmax](https://github.com/axolotl-ai-cloud/axolotl/pull/3338), improves long context in attention.
- 2025/12:
  - Axolotl now includes support for [Kimi-Linear](https://docs.axolotl.ai/docs/models/kimi-linear.html), [Plano-Orchestrator](https://docs.axolotl.ai/docs/models/plano.html), [MiMo](https://docs.axolotl.ai/docs/models/mimo.html), [InternVL 3.5](https://docs.axolotl.ai/docs/models/internvl3_5.html), [Olmo3](https://docs.axolotl.ai/docs/models/olmo3.html), [Trinity](https://docs.axolotl.ai/docs/models/trinity.html), and [Ministral3](https://docs.axolotl.ai/docs/models/ministral3.html).
  - [Distributed Muon Optimizer](https://github.com/axolotl-ai-cloud/axolotl/pull/3264) support has been added for FSDP2 pretraining.
- 2025/10: New model support has been added in Axolotl for: [Qwen3 Next](https://docs.axolotl.ai/docs/models/qwen3-next.html), [Qwen2.5-vl, Qwen3-vl](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/qwen2_5-vl), [Qwen3, Qwen3MoE](https://docs.axolotl.ai/docs/models/qwen3.html), [Granite 4](https://docs.axolotl.ai/docs/models/granite4.html), [HunYuan](https://docs

...
*(Truncated for Knowledge Vault)*