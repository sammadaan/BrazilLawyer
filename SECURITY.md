# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Supported       |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities via email to: aseemmadaan9@gmail.com

Include as much information as possible:
- Type of issue (e.g. buffer overflow, SQL injection, XSS, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- Location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

## Security Features

mais petiçoes implements several security measures:

- Environment variable management for sensitive data
- Input validation for all API endpoints
- SQL injection prevention with SQLAlchemy ORM
- Rate limiting for API endpoints and scrapers
- Secure database connection handling
- Docker containerization for isolation

## Legal Data Handling

Given the sensitive nature of legal data:
- All data is handled in compliance with LGPD (Brazilian Data Protection Law)
- No personal information is stored without explicit consent
- All database communications are encrypted
- Regular security audits are recommended for production deployments

## Updates

Security updates will be released as soon as possible. Subscribe to GitHub notifications to stay informed.
