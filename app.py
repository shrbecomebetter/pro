import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 设置页面配置
st.set_page_config(
    page_title="AI指令优化工具",
    page_icon="⚡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 初始化session state
if 'history' not in st.session_state:
    st.session_state.history = []

# 自定义CSS样式
st.markdown("""
<style>
    /* 全局样式 */
    .block-container {
        padding: 3rem 1rem !important;
        max-width: 1000px !important;
    }
    
    .main > div {
        padding: 0 !important;
    }
    
    .stApp {
        background: #ffffff;
    }
    
    .main-container {
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* 标题样式 */
    .header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .header h1 {
        color: #000000;
        font-size: 2.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    .header p {
        color: #666;
        font-size: 1.1rem;
    }
    
    /* 输入区域样式 */
    .input-container {
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        background: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        margin-bottom: 1rem;
    }
    
    /* 输入框样式 */
    .stTextArea > label {
        display: none !important;
    }
    
    .stTextArea textarea {
        border: none !important;
        padding: 1.5rem !important;
        min-height: 180px !important;
        font-size: 1.2rem !important;
        line-height: 1.6 !important;
        color: #1f2937 !important;
        background: transparent !important;
        font-family: inherit !important;
    }
    
    .stTextArea textarea:focus {
        box-shadow: none !important;
        border: none !important;
    }
    
    /* 按钮样式 */
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #FF8E53) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 2.5rem !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        border-radius: 30px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.2) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.3) !important;
    }
    
    .stButton > button:active {
        transform: translateY(1px) !important;
    }
    
    /* 结果区域样式 */
    .output-container {
        margin-top: 2rem;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        background: #ffffff;
        padding: 2rem;
    }
    
    .output-title {
        color: #000000;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #e5e7eb;
    }
    
    .output-content {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #1f2937;
    }
</style>
""", unsafe_allow_html=True)

# 页面内容
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# 标题区域
st.markdown("""
<div class="header">
    <h1>AI指令优化工具</h1>
    <p>输入您的指令，获得更专业的表达</p>
</div>
""", unsafe_allow_html=True)

# 输入区域
st.markdown('<div class="input-container">', unsafe_allow_html=True)
user_prompt = st.text_area(
    label="输入指令",
    placeholder="请输入您想要优化的AI指令...",
    key="input",
    label_visibility="collapsed"
)

# 按钮区域
col1, col2, col3 = st.columns([4,2,4])
with col2:
    if st.button("✨ 优化指令", key="optimize_button"):
        if user_prompt:
            # 注入自定义加载动画
            st.markdown("""
                <style>
                @keyframes custom-spin {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }
                .loading-container {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    gap: 8px;
                    padding: 10px 20px;
                    background: rgba(255, 255, 255, 0.9);
                    border-radius: 40px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
                    white-space: nowrap;
                    margin: 10px auto;
                    min-width: 200px;
                }
                .custom-spinner {
                    min-width: 24px;
                    width: 24px;
                    height: 24px;
                    border: 2.5px solid transparent;
                    border-radius: 50%;
                    border-top-color: #FF6B6B;
                    border-right-color: #FF8E53;
                    border-bottom-color: #FF6B6B;
                    border-left-color: #FF8E53;
                    animation: custom-spin 1s linear infinite;
                }
                .loading-text {
                    color: #FF6B6B;
                    font-size: 1rem;
                    font-weight: 500;
                    white-space: nowrap;
                    overflow: hidden;
                    text-overflow: ellipsis;
                }
                </style>
                <div style="text-align: center;">
                    <div class="loading-container">
                        <div class="custom-spinner"></div>
                        <span class="loading-text">✨ 施展优化魔法中</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            try:
                from prompt import optimize_prompt
                optimized_prompt = optimize_prompt(user_prompt)
                if optimized_prompt:
                    if "发生错误" in optimized_prompt or "API密钥配置错误" in optimized_prompt or "连接API服务器失败" in optimized_prompt:
                        st.error(optimized_prompt)
                    else:
                        st.session_state.history.insert(0, {
                            'input': user_prompt,
                            'output': optimized_prompt,
                            'timestamp': pd.Timestamp.now()
                        })
                        st.session_state.optimized_result = optimized_prompt
            except Exception as e:
                st.error(f"✋ 糟糕！优化过程遇到了问题：{str(e)}")
        else:
            st.warning("💡 请输入需要优化的指令")
st.markdown('</div>', unsafe_allow_html=True)

# 输出区域
if 'optimized_result' in st.session_state:
    st.markdown('<div class="output-container">', unsafe_allow_html=True)
    st.markdown('<div class="output-title">优化结果</div>', unsafe_allow_html=True)
    
    # 解析优化结果
    result_parts = st.session_state.optimized_result.split('##')
    optimized_prompt = result_parts[1].replace('优化后的指令\n', '').strip()
    optimization_explanation = result_parts[2].replace('优化说明\n', '').strip() if len(result_parts) > 2 else ''
    optimization_points = result_parts[3].replace('优化要点\n', '').strip() if len(result_parts) > 3 else ''
    
    # 显示核心指令
    st.code(optimized_prompt, language=None)
    
    # 优化说明
    if optimization_explanation:
        with st.expander("优化说明"):
            st.markdown(optimization_explanation)
    
    # 优化要点
    if optimization_points:
        with st.expander("优化要点"):
            st.markdown(optimization_points)
    
    st.markdown('</div>', unsafe_allow_html=True)

# 历史记录区域
if st.session_state.history:
    st.markdown("### 历史记录")
    for idx, item in enumerate(st.session_state.history):
        # 使用列来组织布局
        with st.container():
            st.markdown(f"""
            <div style="
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 1.5rem;
                margin-bottom: 1rem;
                background: white;
            ">
                <div style="font-weight: 500; margin-bottom: 1rem; color: #374151;">
                    优化记录 {idx + 1}
                </div>
            """, unsafe_allow_html=True)
            
            # 显示原始指令
            st.markdown("**原始指令**")
            st.text(item['input'])
            
            # 解析并显示优化结果
            result_parts = item['output'].split('##')
            if len(result_parts) > 1:
                optimized_prompt = result_parts[1].replace('优化后的指令\n', '').strip()
                st.markdown("**优化结果**")
                st.code(optimized_prompt, language=None)
                
                # 如果需要显示优化说明和要点
                if len(result_parts) > 2:
                    optimization_explanation = result_parts[2].replace('优化说明\n', '').strip()
                    optimization_points = result_parts[3].replace('优化要点\n', '').strip() if len(result_parts) > 3 else ''
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if optimization_explanation:
                            with st.expander("查看优化说明"):
                                st.markdown(optimization_explanation)
                    with col2:
                        if optimization_points:
                            with st.expander("查看优化要点"):
                                st.markdown(optimization_points)
            
            st.markdown("</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)