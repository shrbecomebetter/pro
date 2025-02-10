import os
import openai
import re
from typing import List, Dict, Optional

class InstructionOptimizer:
    def __init__(self):
        # 从环境变量获取API密钥
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("未找到 OPENAI_API_KEY 环境变量")
            
        self.client = openai.OpenAI(
            api_key=self.api_key,
            base_url=os.getenv('OPENAI_API_BASE', 'https://api.siliconflow.cn/v1/')
        )
        
        self.system_prompt = """你是一个资深的AI指令优化专家，专门帮助用户提炼精准的AI指令。
        
        你的优化流程：
        1. 【指令分析】识别原始指令的核心需求
        2. 【问题诊断】指出表述不清晰、歧义或效率低下的部分
        3. 【优化方案】提供结构化改进方案（使用明确的分步说明）
        4. 【优化要点】用3个关键点说明改进优势
        
        输出格式要求：
        ## 优化后的指令
        {优化后的指令内容}
        
        ## 优化说明
        {分步骤说明优化策略}
        
        ## 优化要点
        - 要点1：...
        - 要点2：... 
        - 要点3：..."""
        
        self.context: List[Dict] = [{'role': 'system', 'content': self.system_prompt}]
        self.thinking_buffer: str = ""
        self.last_thought: Optional[str] = None
        self.response_buffer: str = ""

    def _process_think_tag(self, content: str) -> None:
        """处理包含<thinking>标签的内容"""
        if '<thinking>' in content.lower():
            self.thinking_buffer = ""
            content = content.split('<thinking>')[-1]
            
        if '</thinking>' in content.lower():
            self.thinking_buffer += content.split('</thinking>')[0]
            self.last_thought = self.thinking_buffer.strip()
            self.thinking_buffer = ""
        elif self.thinking_buffer:
            self.thinking_buffer += content

    def _process_stream_response(self, response) -> str:
        """处理流式响应并返回可视化内容"""
        final_output = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                
                # 处理思考内容
                #self._process_think_tag(content)
                
                # 构建最终输出
                #if not self.thinking_buffer:
                final_output += content
                print(content, end='', flush=True)
        
        return final_output

    def optimize_instruction(self, original_instruction: str) -> str:
        """优化用户指令的核心方法"""
        try:
            if not original_instruction.strip():
                return "请提供需要优化的指令内容"
                
            self.context.append({'role': 'user', 'content': f"请优化这个指令：{original_instruction}"})
            
            response = self.client.chat.completions.create(
                model=os.getenv('MODEL'),
                messages=self.context,
                temperature=0.7,
                stream=True
            )
            
            print("\n【优化过程】")
            final_output = self._process_stream_response(response)
            
            if not final_output:
                return "优化过程未能生成有效结果，请重试"
                
            self.context.append({'role': 'assistant', 'content': final_output})
            return final_output
            
        except Exception as e:
            print(f"\n⚠️ 详细错误信息：{str(e)}")
            if "api_key" in str(e).lower():
                return "API密钥配置错误，请检查环境变量设置"
            elif "connection" in str(e).lower():
                return "连接API服务器失败，请检查网络设置"
            else:
                return f"发生错误：{str(e)}"

def optimize_prompt(prompt_text):
    optimizer = InstructionOptimizer()
    return optimizer.optimize_instruction(prompt_text)
