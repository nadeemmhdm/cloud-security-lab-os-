const labs=[
["01","Cloud Security Fundamentals","Local Practical Lab","Cloud computing, service models, shared responsibility, IAM, networking, storage and security tools.","01-cloud-security-fundamentals.md"],
["02","AWS Identity & Access Security","Local Practical Equivalent","IAM, users, roles, policies, least privilege, access keys and permission review.","02-aws-identity-access-security.md"],
["03","AWS Network Security","Local Practical Equivalent","VPC, subnets, security groups, NACL concepts, exposure and monitoring.","03-aws-network-security.md"],
["04","AWS Compute Security","Local Practical Equivalent","EC2 concepts, open ports, patching, metadata, containers and hardening.","04-aws-compute-security.md"],
["05","AWS Storage & Data Security","Local Practical Equivalent","S3 concepts, public access, permissions, encryption, protection and snapshots.","05-aws-storage-data-security.md"],
["06","Microsoft Azure Security","Local Practical Equivalent","Entra ID, IAM, networking, storage, compute and monitoring concepts.","06-microsoft-azure-security.md"],
["07","Microsoft Sentinel & SIEM","Local SIEM Practical","SIEM, ingestion, detections, alerts and incident investigation using local telemetry.","07-microsoft-sentinel-siem.md"],
["08","KQL for Security Analysis","Local Query Practical","Filtering, searching, sorting, aggregation and log investigation; not Microsoft's KQL engine.","08-kql-security-analysis.md"],
["09","Microsoft Defender XDR","Local XDR Concept Practical","Threat detection and investigation concepts across XDR syllabus categories.","09-microsoft-defender-xdr.md"]];
document.querySelector("#labgrid").innerHTML=labs.map(x=>`<article class="lab"><small>MODULE ${x[0]} · ${x[2]}</small><h3>${x[1]}</h3><p>${x[3]}</p><a href="../labs/${x[4]}">Open solution guide →</a></article>`).join("");
document.querySelectorAll(".tab").forEach(b=>b.onclick=()=>{document.querySelectorAll(".tab,.codepanel").forEach(x=>x.classList.remove("active"));b.classList.add("active");document.querySelector("#"+b.dataset.tab).classList.add("active")});
document.querySelector("#menu").onclick=()=>document.querySelector("#nav").classList.toggle("open");document.querySelectorAll("#nav a").forEach(a=>a.onclick=()=>document.querySelector("#nav").classList.remove("open"));