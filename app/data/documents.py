from langchain_core.documents import Document

def load_documents():
    return [
        Document(
            page_content="We provide AI-powered business automation, internal tools, and intelligent chat systems for companies.",
            metadata={"topic": "services"}
        ),
        Document(
            page_content="Project pricing usually ranges between $5,000 and $25,000 depending on complexity, integrations, and scope.",
            metadata={"topic": "pricing"}
        ),
        Document(
            page_content="API integrations may increase cost depending on security, data volume, and third-party dependencies.",
            metadata={"topic": "integration"}
        ),
        Document(
            page_content="Typical project timelines range from 4 to 8 weeks including discovery, development, and testing.",
            metadata={"topic": "timeline"}
        ),
        Document(
            page_content="We integrate with CRMs, internal APIs, databases, and cloud services using secure authentication.",
            metadata={"topic": "tech"}
        ),
    ]
